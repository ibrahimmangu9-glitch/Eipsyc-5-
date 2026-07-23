import { useQuery } from '@tanstack/react-query'
import apiClient from '../services/api'
import Loading from '../components/Loading'
import Error from '../components/Error'

interface Country {
  id: number
  name: string
  code: string
  capital?: string
  region?: string
  currency?: string
}

const Countries = () => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['countries'],
    queryFn: async () => {
      const response = await apiClient.get('/api/v1/countries')
      return response.data
    }
  })

  if (isLoading) return <Loading />
  if (error) return <Error message="Failed to load countries" />

  return (
    <div className="container mx-auto py-12">
      <h1 className="text-4xl font-bold mb-8">African Countries</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {data?.countries?.map((country: Country) => (
          <div key={country.id} className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition">
            <h2 className="text-2xl font-bold mb-2">{country.name}</h2>
            <p className="text-gray-600 mb-2"><strong>Code:</strong> {country.code}</p>
            {country.capital && <p className="text-gray-600 mb-2"><strong>Capital:</strong> {country.capital}</p>}
            {country.region && <p className="text-gray-600 mb-2"><strong>Region:</strong> {country.region}</p>}
            {country.currency && <p className="text-gray-600"><strong>Currency:</strong> {country.currency}</p>}
          </div>
        ))}
      </div>
    </div>
  )
}

export default Countries