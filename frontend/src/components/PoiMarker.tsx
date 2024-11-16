import { AdvancedMarker } from "@vis.gl/react-google-maps";

type PoiMarkerProps = {
  name: string,
  position: {
    lat: number,
    lng: number
  }
}

const PoiMarker = ({ name, position }: PoiMarkerProps) => {
  return (
    <AdvancedMarker
      key={name}
      position={position}
    >
      <div
        style={{
          position: 'absolute',
          top: '-10px',
          left: '10px',
          backgroundColor: '#FFFFFF',
          color: '#000000',
          padding: '2px 6px',
          borderRadius: '4px',
          fontSize: '12px',
          fontWeight: 'bold',
          whiteSpace: 'nowrap',
          pointerEvents: 'none'
        }}
      >
        {name}
      </div>
      <div
        style={{
          width: '8px',
          height: '8px',
          backgroundColor: '#000',
          borderRadius: '50%',
          border: '2px solid #FFFFFF',
        }}
      />
    </AdvancedMarker>
  );
};

export default PoiMarker
