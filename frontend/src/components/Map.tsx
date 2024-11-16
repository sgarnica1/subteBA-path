import { useEffect, useMemo, useState } from 'react';
import {
  APIProvider,
  Map,
} from "@vis.gl/react-google-maps";
import PoiMarker from './PoiMarker';
import Polylines from './Polylines';
import { PositionType, StationsType } from '../types/types';

const GOOGLE_MAPS_API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

const SubteMap = () => {
  const [stations, setStations] = useState<StationsType[]>([]);
  const [lineNames, setLineNames] = useState<string[]>([]);

  const [location] = useState<PositionType>({
    lat: -34.6098887,
    lng: -58.4034423
  });

  const mapOptions = {
    zoomControl: true,
    scrollwheel: true,
    clickableIcons: true,
    disableDefaultUI: false
  };

  useEffect(() => {
    if (stations.length == 0 && lineNames.length == 0)
      fetch("http://localhost:8000/api/stations")
        .then(res => res.json())
        .then(data => {
          if (data?.lines) setLineNames(Object.values(data.lines));
          if (data?.stations) {
            const formatted = Object.values(data.stations).map((station: any) => ({
              name: station.name,
              position: { lat: station.position[0], lng: station.position[1] },
              line: station.line
            }));
            setStations(formatted);
          }
        });
  }, [stations, lineNames]);

  const stationsByLine = useMemo(() => {
    return stations.reduce((acc, station) => {
      if (!acc[station.line]) acc[station.line] = [];
      acc[station.line].push(station.position);
      return acc;
    }, {} as { [key: string]: PositionType[] });
  }, [stations]);

  return (
    <div className="absolute inset-0">
      <APIProvider apiKey={GOOGLE_MAPS_API_KEY}>
        <Map
          mapId="b02d85ede98fd2bc"
          defaultCenter={location}
          defaultZoom={14}
          gestureHandling="greedy"
          options={mapOptions}
          style={{ width: '100%', height: '100%' }}
        >
          <Polylines stationsByLine={stationsByLine} />

          {stations.map((station) => (
            <PoiMarker name={station.name} position={station.position} />
          ))}
        </Map>
      </APIProvider>
    </div>
  );
};

export default SubteMap;