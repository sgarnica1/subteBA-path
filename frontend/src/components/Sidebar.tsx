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

  const { setShortestPath } = useSubte()

  const getShortestPath = () => {
    fetch(`http://localhost:8000/api/path/?start_position=${origin}&final_position=${destiny}`)
      .then(res => res.json())
      .then(data => {
        const formatted = Object.values(data.path).map((station: any) => ({
          id: station.id,
          name: station.name,
          position: { lat: station.position[0], lng: station.position[1] },
          line: station.line
        }));
        setShortestPath(formatted)

        const routeSteps: Step[] = data.path.map((station: StationsType, index: number) => {
          const mode = index > 0 && data.path[index - 1].line != station.line ? "walking" : "bus"

          return {
            time: index,
            mode: mode,
            description: station.name,
            details: station.line,
            lineColor: getLineColor(station.line)
          }
        })
        setSteps(routeSteps)
      })
  }


  return (
    <div className="min-w-[200px] w-[25%] h-full bg-white text-gray-900 p-6 overflow-y-auto">
      <h2 className="text-xl font-bold mb-4">Subte Buenos Aires</h2>
      <div className='flex flex-col gap-2'>
        <Select options={options} onChange={(e) => setOrigin(e?.value)} placeholder={"Elige un punto de partida"} />
        <Select options={options} onChange={(e) => setDestiny(e?.value)} placeholder={"Elige un lugar de destino"} />
        <button className='mt-5 p-2 text-white bg-slate-500 rounded-md' onClick={() => getShortestPath()}>Buscar ruta</button>
      </div>
      <div className="flex flex-col gap-2 mt-5">
        {steps &&
          <RouteDisplay routeSteps={steps} />
        }
      </div>


    </div>
  );
};

export default Sidebar;
