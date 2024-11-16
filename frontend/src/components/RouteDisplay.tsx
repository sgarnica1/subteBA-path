import { FaWalking, FaBus } from "react-icons/fa"; // Import icons
import { Step } from '../types/types';


const routeSteps: Step[] = [
  {
    time: "5:41 p.m.",
    mode: "walking",
    description: "Tu ubicación",
    details: "A pie, aproximadamente 1 min, 52 metros",
  },
  {
    time: "5:42 p.m.",
    mode: "bus",
    description: "Las Meninas",
    details: "484 Santa Rosa-Est. Leganés Central, 2 min (3 paradas)",
    lineColor: "green", // Bus-specific line color
  },
  {
    time: "5:44 p.m.",
    mode: "walking",
    description: "Vía Lusitana-Cementerio Sur",
    details: "A pie, aproximadamente 8 min, 550 metros",
  },
  {
    time: "5:52 p.m.",
    mode: "walking",
    description: "Iglesia evangélica Salem",
    details: "Calle del Cidro, 8, Carabanchel, 28044 Madrid",
  },
];

type RouteDisplayProps = {
  routeSteps: Step[]
}

const RouteDisplay = ({ routeSteps }: RouteDisplayProps) => {
  return (
    <div className="flex flex-col gap-4 p-4">
      {routeSteps.map((step, index) => (
        <div key={index} className="flex items-start gap-4">
          {/* Time Column */}
          <div className="text-gray-500 text-sm w-[80px]">{step.time}</div>

          {/* Line and Content */}
          <div className="flex flex-col items-center">
            {/* Icon */}
            <div className="flex items-center justify-center w-8 h-8 rounded-full bg-gray-100 text-blue-500">
              {step.mode === "walking" ? <FaWalking /> : <FaBus />}
            </div>

            {/* Vertical Line */}
            {index < routeSteps.length - 1 && (
              <div
                className={`w-[2px] h-12 ${step.lineColor ? `bg-${step.lineColor}-500` : "bg-gray-300"
                  }`}
              ></div>
            )}
          </div>

          {/* Description */}
          <div className="flex flex-col">
            <p className="font-bold">{step.description}</p>
            <p className="text-sm text-gray-600">{step.details}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default RouteDisplay;
