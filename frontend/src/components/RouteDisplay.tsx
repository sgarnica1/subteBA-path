import { FaSubway, FaWalking } from "react-icons/fa"; // Import icons
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
            <div className="mt-2 text-blue-500">
              {step.mode == "walking" ? <FaWalking /> : <FaSubway className='text-white' />}
            </div>

            {/* Line and Content */}
            <div className="flex flex-col items-center">
              {/* Icon */}
              <div className="w-4 h-4 rounded-full bg-white border-black border-2"></div>
              {/* Vertical Line */}
              {index < routeSteps.length - 1 && (
                <div
                  className={`w-[3px] h-[70px] ${step.mode === "walking"
                    ? `bg-transparent border-l-4 border-dotted border-blue-walking`
                    : step.lineColor
                      ? `bg-${step.lineColor}`
                      : "bg-gray-500"
                    }`}
                ></div>

              )}
            </div>

            {/* Description */}
            <div className="flex flex-col mb-5">
              <p className="font-bold text-xs">{step.description}</p>
              <p className="text-sm text-gray-600">{step.mode == "walking" ? "Transbordar a la siguiente línea" : step.details}</p>
              {step.time > 0 ? <p className='text-gray-500 text-xs'>({step.time} minutos)</p> : ""}

            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default RouteDisplay;
