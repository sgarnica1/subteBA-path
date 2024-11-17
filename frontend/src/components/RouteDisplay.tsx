import { FaWalking, FaBus } from "react-icons/fa"; // Import icons
import { Step } from '../types/types';

type RouteDisplayProps = {
  routeSteps: Step[]
}

const RouteDisplay = ({ routeSteps }: RouteDisplayProps) => {
  return (
    <div className="flex flex-col gap-4 p-4">
      {routeSteps.map((step, index) => (
        <div key={index} className="flex items-start gap-4">
          {/* Time Column */}
          <div className="text-gray-500 text-sm min-w-[30px]">{step.time}</div>

          {/* Line and Content */}
          <div className="flex flex-col items-center">
            {/* Icon */}
            <div className="flex items-center justify-center w-8 h-8 rounded-full bg-gray-100 text-blue-500">
              {step.mode === "walking" ? <FaWalking /> : <FaBus />}
            </div>

            {/* Vertical Line */}
            {index < routeSteps.length - 1 && (
              <div
                className={`w-[3px] h-12 ${step.lineColor ? `bg-[${step.lineColor}]` : "bg-gray-500"
                  }`}
              ></div>
            )}
          </div>

          {/* Description */}
          <div className="flex flex-col">
            <p className="font-bold text-xs">{step.description}</p>
            <p className="text-sm text-gray-600">{step.details}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default RouteDisplay;
