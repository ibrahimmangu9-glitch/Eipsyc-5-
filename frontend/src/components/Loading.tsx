const Loading = () => {
  return (
    <div className="container mx-auto py-12 text-center">
      <div className="inline-block animate-spin">
        <div className="w-12 h-12 border-4 border-primary border-t-accent rounded-full"></div>
      </div>
      <p className="mt-4 text-gray-600">Loading...</p>
    </div>
  )
}

export default Loading