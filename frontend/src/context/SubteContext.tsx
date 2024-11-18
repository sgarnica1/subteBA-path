import { createContext, ReactNode, useContext, useEffect, useState } from 'react';
import { StationsType } from '../types/types';

interface SubteContextType {
  shortestPath: StationsType[]
  setShortestPath: (stations: StationsType[]) => void,
  stations: StationsType[]
  setStations: (stations: StationsType[]) => void,
  lineNames: string[]
  setLineNames: (stations: string[]) => void,
}

const defaultContext: SubteContextType = {
  shortestPath: [],
  stations: [],
  lineNames: [],
  setShortestPath: () => { },
  setStations: () => { },
  setLineNames: () => { },
};

const SubteContext = createContext<SubteContextType>(defaultContext)

const useSubte = () => useContext(SubteContext)

const SUBTE_API_URL = import.meta.env.VITE_SUBTE_API_URL

type SubteProviderProps = {
  children: ReactNode
}

const SubteProvider = ({ children }: SubteProviderProps) => {
  const [stations, setStations] = useState<StationsType[]>([]);
  const [lineNames, setLineNames] = useState<string[]>([]);
  const [shortestPath, setShortestPath] = useState<StationsType[]>([])



  useEffect(() => {
    if (stations.length == 0 && lineNames.length == 0)
      fetch(`${SUBTE_API_URL}/stations`)
        .then(res => res.json())
        .then(data => {
          if (data?.lines) setLineNames(Object.values(data.lines));
          if (data?.stations) {
            const formatted = Object.values(data.stations).map((station: any) => ({
              id: station.id,
              name: station.name,
              position: { lat: station.position[0], lng: station.position[1] },
              line: station.line
            }));
            setStations(formatted);
          }
        });
  }, [stations, lineNames]);

  return (
    <SubteContext.Provider
      value={{
        shortestPath,
        stations,
        lineNames,
        setShortestPath,
        setStations,
        setLineNames
      }}
    >
      {children}
    </SubteContext.Provider>
  )
}

export { useSubte, SubteProvider }