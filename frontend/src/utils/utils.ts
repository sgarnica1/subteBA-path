import { option } from '../types/types'
import { days, hours, lineColors, tailwindLineColors } from './data'

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

export const getCurrentDay = () => {
  const today = new Date().getDay()
  let day: option = days.MONDAY
  switch (today) {
    case 1:
      day = days.MONDAY
      break
    case 2:
      day = days.TUESDAY
      break
    case 3:
      day = days.WEDNESDAY
      break
    case 4:
      day = days.THURSDAY
      break
    case 5:
      day = days.FRIDAY
      break
    case 6:
      day = days.SATURDAY
      break
    case 7:
      day = days.SUNDAY
      break
    default:
      day = days.MONDAY
  }

  return day
}

export const getCurrentHour = () => {
  let hour: number = new Date().getHours()
  if (hour < 8 || hour > 22) hour = 8
  return hours[hour.toString()]
}