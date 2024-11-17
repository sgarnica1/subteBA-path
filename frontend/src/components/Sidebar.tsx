import { useState } from 'react';
import Select from 'react-select';
import RouteDisplay from './RouteDisplay';
import { StationsType, Step } from '../types/types';
import { useSubte } from '../context/SubteContext';
import { getLineColor } from '../utils/data';

type SidebarProps = {
  options: {
    value: string,
    label: string
  }[]
}

const Sidebar = ({ options }: SidebarProps) => {
  const [origin, setOrigin] = useState<string>("")
  const [destiny, setDestiny] = useState<string>("")
  const [steps, setSteps] = useState<Step[]>([])
  const [totalTime, setTotalTime] = useState<number | null>(null)

  const { setShortestPath } = useSubte()

  const getShortestPath = () => {
    if (origin == "" || destiny == "") return

    fetch(`http://localhost:8000/api/path/?start_position=${origin}&final_position=${destiny}`)
      .then(res => res.json())
      .then(data => {
        console.log(data)
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
  }


  return (
    <div className="min-w-[200px] lg:w-[22%] md:w-[36%] h-full bg-white text-gray-900 p-6 overflow-y-auto">
      <h2 className="text-xl font-bold mb-4">Subte Buenos Aires</h2>
      <div className='flex flex-col gap-2'>
        <Select options={options} onChange={(e) => e && setOrigin(e.value)} placeholder={"Elige un punto de partida"} />
        <Select options={options} onChange={(e) => e && setDestiny(e.value)} placeholder={"Elige un lugar de destino"} />
        <button className='mt-5 p-2 text-white bg-slate-500 rounded-md' onClick={() => getShortestPath()}>Buscar ruta</button>
      </div>
      <div className="flex flex-col gap-2 mt-5">
        {steps && totalTime &&
          <RouteDisplay routeSteps={steps} totalTime={totalTime} />
        }
      </div>


    </div>
  );
};

export default Sidebar;
