import { useMap } from '@vis.gl/react-google-maps';
import { useEffect, useRef } from 'react';
import { PositionType } from '../types/types';

const Polylines = ({ stationsByLine }: { stationsByLine: { [key: string]: PositionType[] } }) => {
  const map = useMap();
  const polylinesRef = useRef<google.maps.Polyline[]>([]);

  useEffect(() => {
    if (!map || !window.google) return;

    polylinesRef.current.forEach(line => line.setMap(null));
    polylinesRef.current = [];

    Object.entries(stationsByLine).forEach(([line, positions]) => {
      const polyline = new google.maps.Polyline({
        path: positions,
        geodesic: true,
        strokeColor:
          line === "Línea A" ? "#04ACDF" :
            line === "Línea B" ? "#EE1B2E" :
              line === "Línea C" ? "#0168B3" :
                line === "Línea D" ? "#008067" :
                  line === "Línea E" ? "#6D227F" :
                    "#000000",
        strokeOpacity: 1.0,
        strokeWeight: 5,
        map: map
      });
      polylinesRef.current.push(polyline);
    });

    // Cleanup
    return () => {
      polylinesRef.current.forEach(line => line.setMap(null));
      polylinesRef.current = [];
    };
  }, [map, stationsByLine]);

  return null;
};

export default Polylines