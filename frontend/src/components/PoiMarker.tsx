import { useState } from "react";
import { AdvancedMarker } from "@vis.gl/react-google-maps";
import SubteIcon from '../assets/subte.png';
import PinIcon from '../assets/pin.svg';

type PoiMarkerProps = {
  name: string;
  position: {
    lat: number;
    lng: number;
  };
  isOrigin?: boolean,
};

const PoiMarker = ({ name, position, isOrigin = false }: PoiMarkerProps) => {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <AdvancedMarker
      key={name}
      position={position}
      onClick={() => { }}
    >
      {/* Tooltip */}
      {isHovered && (
        <div
          style={{
            position: 'absolute',
            top: '-30px',
            left: '50%',
            transform: 'translateX(-50%)',
            backgroundColor: '#FFFFFF',
            color: '#000000',
            padding: '4px 8px',
            borderRadius: '4px',
            fontSize: '12px',
            fontWeight: 'bold',
            whiteSpace: 'nowrap',
            boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
            pointerEvents: 'none',
            zIndex: 10,
          }}
        >
          {name}
        </div>
      )}

      {/* Pin */}
      {!isOrigin &&
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

      {isOrigin &&
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
