import axios from "axios";

export type Alert = {
  id: string;
  employee: { id: string; name: string };
  severity: "low"|"medium"|"high";
  category: string;
  created_at: string;
  status: "open"|"dismissed";
};

const client = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000"
});

export async function fetchAlerts(params: Record<string, any>) {
  const r = await client.get<Alert[]>("/api/alerts", { params });
  return r.data;
}

export async function dismissAlert(id: string) {
  const r = await client.post<Alert>(`/api/alerts/${id}/dismiss`);
  return r.data;
}
