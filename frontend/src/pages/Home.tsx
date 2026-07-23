import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <div className="min-h-[calc(100vh-200px)]">
      <div className="bg-gradient-to-r from-secondary to-primary text-white py-20">
        <div className="container mx-auto text-center">
          <h1 className="text-5xl font-bold mb-4">Welcome to EIPSYC5 AFRICA</h1>
          <p className="text-2xl mb-8">ONE AFRICA. ONE PLATFORM. INFINITE JOURNEYS.</p>
          <div className="flex gap-4 justify-center">
            <Link to="/destinations" className="bg-accent text-secondary px-8 py-3 rounded-lg font-bold hover:opacity-90">
              Explore Destinations
            </Link>
            <Link to="/accommodations" className="bg-white text-secondary px-8 py-3 rounded-lg font-bold hover:opacity-90">
              Find Accommodations
            </Link>
          </div>
        </div>
      </div>
      <div className="container mx-auto py-16">
        <h2 className="text-3xl font-bold mb-8 text-center">Featured Experiences</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-bold mb-3">Safari Adventures</h3>
            <p>Explore the African wilderness with expert guides.</p>
          </div>
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-bold mb-3">Beach Escapes</h3>
            <p>Relax on pristine African beaches.</p>
          </div>
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-bold mb-3">Cultural Tours</h3>
            <p>Experience authentic African cultures.</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home