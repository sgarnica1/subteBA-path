export const lineColors = {
  "LINEA_A": "#04ACDF",
  "LINEA_B": "#EE1B2E",
  "LINEA_C": "#0168B3",
  "LINEA_D": "#008067",
  "LINEA_E": "#6D227F",
  "DEFAULT": "#000000"
}

export const tailwindLineColors = {
  "LINEA_A": "cyan-line-a",
  "LINEA_B": "red-line-b",
  "LINEA_C": "blue-line-c",
  "LINEA_D": "green-line-d",
  "LINEA_E": "purple-line-e",
  "DEFAULT": "black"
}

export const getLineColor = (line: string, tailwindColors: boolean = false): string => {
  const lineColorosDict = tailwindColors ? tailwindLineColors : lineColors

  let lineColor = lineColorosDict.DEFAULT

  switch (line) {
    case "Línea A":
      lineColor = lineColorosDict.LINEA_A
      break
    case "Línea B":
      lineColor = lineColorosDict.LINEA_B
      break
    case "Línea C":
      lineColor = lineColorosDict.LINEA_C
      break
    case "Línea D":
      lineColor = lineColorosDict.LINEA_D
      break
    case "Línea E":
      lineColor = lineColorosDict.LINEA_E
      break
    default:
      lineColor = lineColorosDict.DEFAULT
  }

  return lineColor
}