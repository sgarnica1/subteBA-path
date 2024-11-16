export type PositionType = {
  lat: number,
  lng: number
}

export type StationsType = {
  name: string,
  position: PositionType,
  line: string
}

export type Step = {
  time: string;
  mode: "walking" | "bus";
  description: string;
  details: string;
  lineColor?: string; // Optional: For different modes of transport
};