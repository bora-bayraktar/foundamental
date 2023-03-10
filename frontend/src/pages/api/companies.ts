// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

export type Company = {
  company_id: number,
  name: string,
  country: string,
  description: string,
  founding_date: string
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Company[]>
) {
  const response = await fetch('http://api:20002/companies');
  const companies = await response.json();
  res.status(200).json(companies);
}
