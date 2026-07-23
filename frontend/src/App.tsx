import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import Home from './pages/Home'
import Countries from './pages/Countries'
import Destinations from './pages/Destinations'
import Accommodations from './pages/Accommodations'
import Layout from './components/Layout'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/countries" element={<Countries />} />
            <Route path="/destinations" element={<Destinations />} />
            <Route path="/accommodations" element={<Accommodations />} />
          </Routes>
        </Layout>
      </Router>
    </QueryClientProvider>
  )
}

export default App