import { useMap } from '@vis.gl/react-google-maps';
import { useEffect, useRef } from 'react';
import { PositionType } from '../types/types';
import { getLineColor } from '../utils/data';

type PolylinesProps = {
  stationsByLine: { [key: string]: PositionType[] }
  strokeOpacity?: number,
  strokeWeight?: number,
  mode?: string
}

const Polylines = ({ stationsByLine, strokeOpacity = 1.0, strokeWeight: strokeWeight = 5, mode = 'walking' }: PolylinesProps) => {
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
        strokeColor: getLineColor(line),
        strokeOpacity: strokeOpacity,
        strokeWeight: strokeWeight,
        map: map
      });
      polylinesRef.current.push(polyline);
    });

    return () => {
      polylinesRef.current.forEach(line => line.setMap(null));
      polylinesRef.current = [];
    };
  }, [map, stationsByLine, strokeOpacity]);

  return null;
};

export default Polylines