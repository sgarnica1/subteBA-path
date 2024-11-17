import { FaWalking, FaBus } from "react-icons/fa"; // Import icons
import { Step } from '../types/types';

type RouteDisplayProps = {
  routeSteps: Step[],
  totalTime: number
}

const RouteDisplay = ({ routeSteps, totalTime }: RouteDisplayProps) => {
  return (
    <>
      {totalTime && totalTime > 0 && (
        <h3 className='text-md text-gray-600 font-semibold'>Tiempo total: {totalTime} minutos</h3>)}
      <div className="flex flex-col p-4">
        {routeSteps.map((step, index) => (
          <div key={index} className="flex items-start gap-4">
            {/* Time Column */}
            <div className="text-gray-500 text-sm min-w-[40px]">{step.time > 0 ? `${step.time} min` : "Fin"}</div>

            {/* Line and Content */}
            <div className="flex flex-col items-center">
              {/* Icon */}
              <div className="flex items-center justify-center w-8 h-8 rounded-full bg-gray-100 text-blue-500">
                {step.mode === "walking" ? <FaWalking /> : <FaBus />}
              </div>

              {/* Vertical Line */}
              {index < routeSteps.length - 1 && (
                <div
                  className={`w-[3px] h-12 ${step.mode === "walking"
                    ? `bg-transparent border-l-4 border-dotted border-blue-walking`
                    : step.lineColor
                      ? `bg-${step.lineColor}`
                      : "bg-gray-500"
                    }`}
                ></div>

              )}
            </div>

            {/* Description */}
            <div className="flex flex-col">
              <p className="font-bold text-xs">{step.description}</p>
              <p className="text-sm text-gray-600">{step.mode == "walking" ? "Caminar a la siguiente estación" : step.details}</p>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default RouteDisplay;
