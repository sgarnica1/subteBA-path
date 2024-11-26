import { useState } from 'react';
import Select from 'react-select';
import RouteDisplay from './RouteDisplay';
import { option, StationsType, Step } from '../types/types';
import { useSubte } from '../context/SubteContext';
import { getLineColor } from '../utils/utils';
import { Oval } from 'react-loader-spinner'

const SUBTE_API_URL = import.meta.env.VITE_SUBTE_API_URL

type SidebarProps = {
  options: option[]
}

const Sidebar = ({ options }: SidebarProps) => {
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<boolean>(false)
  const [origin, setOrigin] = useState<string | null>(null)
  const [destiny, setDestiny] = useState<string | null>(null)
  const [steps, setSteps] = useState<Step[]>([])
  const [totalTime, setTotalTime] = useState<number | null>(null)

  const { setShortestPath, loading: loadingStations, error: errorStations } = useSubte()

  const getShortestPath = () => {
    if (!origin || !destiny) return

    setLoading(true)
    fetch(`${SUBTE_API_URL}/path/?start_position=${origin}&final_position=${destiny}`)
      .then(res => res.json())
      .then(data => {
        setTotalTime(Math.ceil(data.total_time))

        const formatted = Object.values(data.path).map((station: any) => ({
          id: station.id,
          name: station.name,
          position: { lat: station.position[0], lng: station.position[1] },
          line: station.line
        }));
        setShortestPath(formatted)

        const routeSteps: Step[] = data.path.map((station: StationsType, index: number) => {
          const mode = index < data.path.length - 1 && data.path[index + 1].line != station.line ? "walking" : "bus"

          return {
            time: Math.ceil(station.travel_time ? station.travel_time : 0),
            mode: mode,
            description: station.name,
            details: station.line,
            lineColor: getLineColor(station.line, true)
          }
        })
        setSteps(routeSteps)
      })
      .catch(e => setError(e))
      .finally(() => setLoading(false))
  }


  return (
    <div className="min-w-[200px] lg:w-[22%] md:w-[36%] sm:w-[100%] md:h-full h-[50vh] bg-white text-gray-900 p-6 overflow-y-auto">
      <h2 className="text-xl font-bold mb-4">Subte Buenos Aires</h2>
      {loadingStations ?
        <div className='flex gap-3 items-center justify-center'>
          <p>Cargando estaciones...</p>
          <Oval
            visible={true}
            height="20"
            width="20"
            color="#0168B3"
            ariaLabel="oval-loading"
            wrapperStyle={{}}
            wrapperClass=""
          />
        </div> :
        <>
          <div className='flex flex-col gap-2'>
            <Select options={options} onChange={(e) => e && setOrigin(e.value)} placeholder={"Elige un punto de partida"} />
            <Select options={options} onChange={(e) => e && setDestiny(e.value)} placeholder={"Elige un lugar de destino"} />
            {origin && destiny && origin === destiny && (
              <p className="text-sm text-yellow-700 bg-yellow-100 border border-yellow-300 rounded-md p-2 mt-2">
                No se puede seleccionar la misma estación.
              </p>
            )}

            <button
              className='mt-5 p-2 text-white bg-blue-500 hover:bg-blue-400 transition-colors rounded-md disabled:bg-blue-300'
              onClick={() => getShortestPath()}
              disabled={!origin || !destiny || loading || error || origin == destiny ? true : false}
            >
              Buscar ruta
            </button>
            {error || errorStations &&
              <p className="text-sm text-red-600 bg-red-100 border border-red-300 rounded-md p-2 mt-2">
                Ocurrió un error inesperado, por favor vuelve a intentar.
              </p>
            }
          </div>
          <div className="flex flex-col gap-2 mt-5">
            {loading && <div className='w-full flex justify-center content-center'>
              <Oval
                visible={true}
                height="30"
                width="30"
                color="#0168B3"
                ariaLabel="oval-loading"
                wrapperStyle={{}}
                wrapperClass=""
              />
            </div>}
            {!loading && !error && steps && totalTime ?
              <RouteDisplay routeSteps={steps} totalTime={totalTime} /> : <></>
            }
          </div>
        </>}
    </div>
  );
};

export default Sidebar;
