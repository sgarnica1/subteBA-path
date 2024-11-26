import { useEffect, useMemo, useState } from 'react';
import {
  APIProvider,
  Map,
} from "@vis.gl/react-google-maps";
import PoiMarker from './PoiMarker';
import Polylines from './Polylines';
import { PositionType, StationsType } from '../types/types';
import { useSubte } from '../context/SubteContext';

const GOOGLE_MAPS_API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

type SubteMapProps = {
  stations: StationsType[],
}

const SubteMap = ({ stations }: SubteMapProps) => {
  const [location] = useState<PositionType>({
    lat: -34.605798,
    lng: -58.381277
  });
  const [shortestPathCoords, setShortestPathCoords] = useState<{ [key: string]: PositionType[] } | null>(null)
  const [connections, setCononections] = useState<{ [key: string]: PositionType[] } | null>(null)
  const [strokeOpactity, setStrokeOpacity] = useState<number>(1.0)
  const [strokeWeight, setStrokeWeight] = useState<number>(5)

  const { shortestPath, loading, error } = useSubte()

  const formatLines = (stations: StationsType[]) => {
    return stations.reduce((acc, station) => {
      if (!acc[station.line]) acc[station.line] = [];
      acc[station.line].push(station.position);
      return acc;
    }, {} as { [key: string]: PositionType[] });
  }

  const stationsByLine = useMemo(() => {
    return formatLines(stations)
  }, [stations]);

  useEffect(() => {
    if (shortestPath.length > 0) {
      setShortestPathCoords(
        formatLines(shortestPath))
      setStrokeOpacity(0.4)
      setStrokeWeight(2)

      const aux: { [key: string]: PositionType[] } = {}
      shortestPath.forEach((station, index) => {
        if (index < shortestPath.length - 1 && station.line != shortestPath[index + 1].line) {
          aux[index] = [
            { lat: station.position.lat, lng: station.position.lng },
            { lat: shortestPath[index + 1].position.lat, lng: shortestPath[index + 1].position.lng }
          ]
        }
      })
      setCononections(aux)
    }
  }, [shortestPath])

  return (
    <APIProvider apiKey={GOOGLE_MAPS_API_KEY}>
      <Map
        mapId="b02d85ede98fd2bc"
        defaultCenter={location}
        defaultZoom={14}
        gestureHandling="greedy"
        disableDefaultUI={true}
        style={{ width: '100%', height: '100%' }}
      >
        {!loading && !error && shortestPathCoords &&
          <>
            <Polylines stationsByLine={shortestPathCoords} strokeWeight={10} />
            <PoiMarker
              name={shortestPath[0].name}
              position={shortestPath[0].position}
              isOrigin={true}
            />
            <PoiMarker
              name={shortestPath[shortestPath.length - 1].name}
              position={shortestPath[shortestPath.length - 1].position}
              isDestiny={true}
            />
          </>}

        {!loading && !error && connections &&
          <Polylines stationsByLine={connections} strokeWeight={10} mode={"walking"} />}

        {!loading && !error && <Polylines stationsByLine={stationsByLine} strokeOpacity={strokeOpactity} strokeWeight={strokeWeight} />}

        {!loading && !error && stations.map((station) => (
          <PoiMarker name={station.name} position={station.position} key={station.id} />
        ))}
      </Map>
    </APIProvider>
  );
};

export default SubteMap;