export type PositionType = {
  lat: number,
  lng: number
}

export type StationsType = {
  id: string,
  name: string,
  position: PositionType,
  line: string,
  travel_time?: number
}

export type Step = {
  time: number;
  mode: "walking" | "bus";
  description: string;
  details: string;
  lineColor?: string;
};

export type option = {
  value: string,
  label: string
}