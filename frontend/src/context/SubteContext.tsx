import { createContext, ReactNode, useContext, useEffect, useState } from 'react';
import { StationsType } from '../types/types';

interface SubteContextType {
  shortestPath: StationsType[]
  stations: StationsType[]
  lineNames: string[]
  loading: boolean
  error: boolean
  setShortestPath: (stations: StationsType[]) => void,
  setStations: (stations: StationsType[]) => void,
  setLineNames: (stations: string[]) => void,
}

const defaultContext: SubteContextType = {
  shortestPath: [],
  stations: [],
  lineNames: [],
  loading: true,
  error: false,
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
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<boolean>(false)
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
        })
        .catch(e => setError(e))
        .finally(() => setLoading(false))
  }, [stations, lineNames]);

  return (
    <SubteContext.Provider
      value={{
        shortestPath,
        stations,
        lineNames,
        loading,
        error,
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