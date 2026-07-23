import { useQuery } from '@tanstack/react-query'
import apiClient from '../services/api'
import Loading from '../components/Loading'
import Error from '../components/Error'

const Destinations = () => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['destinations'],
    queryFn: async () => {
      const response = await apiClient.get('/api/v1/destinations')
      return response.data
    }
  })

  if (isLoading) return <Loading />
  if (error) return <Error message="Failed to load destinations" />

  return (
    <div className="container mx-auto py-12">
      <h1 className="text-4xl font-bold mb-8">Popular Destinations</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {data?.destinations?.map((dest: any) => (
          <div key={dest.id} className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition">
            <div className="bg-gray-200 h-48"></div>
            <div className="p-6">
              <h2 className="text-2xl font-bold mb-2">{dest.name}</h2>
              <p className="text-gray-600 mb-4">{dest.description}</p>
              {dest.type && <p className="text-sm text-gray-500"><strong>Type:</strong> {dest.type}</p>}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Destinations