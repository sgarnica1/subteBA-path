export const lineColors = {
  "LINEA_A": "#04ACDF",
  "LINEA_B": "#EE1B2E",
  "LINEA_C": "#0168B3",
  "LINEA_D": "#008067",
  "LINEA_E": "#6D227F",
  "DEFAULT": "#000000"
}

export const getLineColor = (line: string): string => {
  let lineColor = lineColors.DEFAULT

  switch (line) {
    case "Línea A":
      lineColor = lineColors.LINEA_A
      break
    case "Línea B":
      lineColor = lineColors.LINEA_B
      break
    case "Línea C":
      lineColor = lineColors.LINEA_C
      break
    case "Línea D":
      lineColor = lineColors.LINEA_D
      break
    case "Línea E":
      lineColor = lineColors.LINEA_E
      break
    default:
      lineColor = lineColors.DEFAULT
  }

  return lineColor
}