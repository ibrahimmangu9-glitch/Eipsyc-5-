import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="bg-secondary text-white p-4 shadow-lg">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">
          EIPSYC5 AFRICA
        </Link>
        <div className="flex gap-6">
          <Link to="/countries" className="hover:text-accent">Countries</Link>
          <Link to="/destinations" className="hover:text-accent">Destinations</Link>
          <Link to="/accommodations" className="hover:text-accent">Accommodations</Link>
        </div>
      </div>
    </nav>
  )
}

export default Navbar