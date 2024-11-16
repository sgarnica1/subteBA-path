import { useEffect, useState } from 'react';
import Layout from './components/Layout'
import SubteMap from './components/Map'
import { StationsType } from './types/types';
import './App.css'


const App = () => {
  const [stations, setStations] = useState<StationsType[]>([]);
  const [lineNames, setLineNames] = useState<string[]>([]);

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

  return (
    <Layout stations={stations}>
      <SubteMap stations={stations} />
    </Layout>
  )
}

export default App
