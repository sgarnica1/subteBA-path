import Layout from './components/Layout'
import SubteMap from './components/Map'
import { useSubte } from './context/SubteContext';
import './App.css'


const App = () => {
  const { stations } = useSubte()

  return (
    <Layout stations={stations}>
      <SubteMap stations={stations} />
    </Layout>
  )
}

export default App
