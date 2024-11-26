import { useState } from "react";
import { AdvancedMarker } from "@vis.gl/react-google-maps";
import PinIcon from '../assets/pin.svg';
import Tooltip from './Tooltip';

type PoiMarkerProps = {
  name: string;
  position: {
    lat: number;
    lng: number;
  };
  isOrigin?: boolean,
  isDestiny?: boolean,
};

const PoiMarker = ({ name, position, isOrigin = false, isDestiny = false }: PoiMarkerProps) => {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <AdvancedMarker
      key={name}
      position={position}
      onClick={() => { }}
    >
      {/* Tooltip */}
      {isHovered && !isOrigin && (
        <Tooltip name={name} />
      )}
      {isOrigin && (
        <Tooltip name={name} />
      )}

      {/* Pin */}
      {!isDestiny &&
        <div
          style={{
            width: '12px',
            height: '12px',
            backgroundColor: '#fff',
            borderRadius: '50%',
            border: '2px solid #000',
            transform: 'translateY(5px)'
          }}
          onMouseEnter={() => setIsHovered(true)}
          onMouseLeave={() => setIsHovered(false)}
        />
      }

      {isDestiny &&
        <img
          src={PinIcon}
          alt="Pin Icon"
          style={{
            width: '34px',
            height: '34px',
            cursor: 'pointer',
          }}
          onMouseEnter={() => setIsHovered(true)}
          onMouseLeave={() => setIsHovered(false)}
        />
      }
    </AdvancedMarker>
  );
};

export default PoiMarker;
