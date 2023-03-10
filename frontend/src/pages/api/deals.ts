// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

export type Deal = {
  id: number,
  funding_amount: number,
  funding_round: string,
  date: string,
  company_id: number,
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Deal[]>
) {
  const response = await fetch('http://api:20002/deals');
  const companies = await response.json();
  res.status(200).json(companies);
}
