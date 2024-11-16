import { useMemo, useState } from 'react';
import {
  APIProvider,
  Map,
} from "@vis.gl/react-google-maps";
import PoiMarker from './PoiMarker';
import Polylines from './Polylines';
import { PositionType, StationsType } from '../types/types';

const GOOGLE_MAPS_API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

type SubteMapProps = {
  stations: StationsType[],
}

const SubteMap = ({ stations }: SubteMapProps) => {
  const [location] = useState<PositionType>({
    lat: -34.605798,
    lng: -58.381277
  });

  const mapOptions = {
    zoomControl: true,
    scrollwheel: true,
    clickableIcons: true,
    disableDefaultUI: false
  };

  const stationsByLine = useMemo(() => {
    return stations.reduce((acc, station) => {
      if (!acc[station.line]) acc[station.line] = [];
      acc[station.line].push(station.position);
      return acc;
    }, {} as { [key: string]: PositionType[] });
  }, [stations]);

  return (
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
  );
};

export default SubteMap;