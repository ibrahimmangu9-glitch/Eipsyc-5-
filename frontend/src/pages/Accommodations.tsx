import { useQuery } from '@tanstack/react-query'
import apiClient from '../services/api'
import Loading from '../components/Loading'
import Error from '../components/Error'

const Accommodations = () => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['accommodations'],
    queryFn: async () => {
      const response = await apiClient.get('/api/v1/accommodations')
      return response.data
    }
  })

  if (isLoading) return <Loading />
  if (error) return <Error message="Failed to load accommodations" />

  return (
    <div className="container mx-auto py-12">
      <h1 className="text-4xl font-bold mb-8">Find Accommodations</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {data?.accommodations?.map((acc: any) => (
          <div key={acc.id} className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition">
            <div className="bg-gray-200 h-48"></div>
            <div className="p-6">
              <h2 className="text-xl font-bold mb-2">{acc.name}</h2>
              <p className="text-accent text-2xl font-bold mb-4">${acc.price_per_night}/{acc.currency}</p>
              <p className="text-gray-600 mb-2">{acc.description}</p>
              <button className="w-full bg-primary text-white py-2 rounded hover:opacity-90">
                Book Now
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Accommodations