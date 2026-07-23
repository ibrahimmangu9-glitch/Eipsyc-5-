export interface Country {
  id: number
  name: string
  code: string
  capital?: string
  region?: string
  currency?: string
  language?: string
  flag_url?: string
  description?: string
}

export interface Destination {
  id: number
  country_id: number
  name: string
  description?: string
  latitude?: number
  longitude?: number
  type?: string
  best_season?: string
  image_url?: string
}

export interface Accommodation {
  id: number
  destination_id: number
  name: string
  type?: string
  description?: string
  price_per_night?: number
  currency: string
  rooms_available?: number
  rating?: number
  image_url?: string
  is_verified: boolean
  is_active: boolean
}

export interface Booking {
  id: string
  accommodation_id: number
  check_in_date: string
  check_out_date: string
  number_of_guests: number
  total_price?: number
  currency: string
  status: string
  special_requests?: string
}