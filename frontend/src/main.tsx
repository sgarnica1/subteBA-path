import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { SubteProvider } from './context/SubteContext.tsx'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <SubteProvider>
      <App />
    </SubteProvider>
  </StrictMode>,
)
