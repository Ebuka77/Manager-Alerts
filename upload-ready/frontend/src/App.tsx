

import React, { useEffect, useState } from "react";
import type { Alert } from "./api";
import { fetchAlerts, dismissAlert} from "./api";

function App() {
  const [scope, setScope] = useState<"direct"|"subtree">("direct");
  const [severity, setSeverity] = useState<string>("");
  const [q, setQ] = useState("");
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [loading, setLoading] = useState(false);

  async function load() {
    setLoading(true);
    try {
      const params: any = { manager_id: "E2", scope };
      if (severity) params.severity = severity;
      if (q) params.q = q;
      const data = await fetchAlerts(params);
      setAlerts(data);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { load(); }, [scope, severity, q]);

  async function onDismiss(id: string) {
    // optimistic update
    const prev = alerts;
    setAlerts(alerts.map(a => a.id === id ? { ...a, status: "dismissed" } : a));
    try {
      await dismissAlert(id);
    } catch (err) {
      // simple rollback
      setAlerts(prev);
      alert("Failed to dismiss");
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Manager Alerts (demo)</h1>

      <div style={{ display: "flex", gap: 12, marginBottom: 12 }}>
        <label>
          Scope:
          <select value={scope} onChange={e => setScope(e.target.value as any)}>
            <option value="direct">Direct</option>
            <option value="subtree">Subtree</option>
          </select>
        </label>

        <label>
          Severity:
          <select value={severity} onChange={e => setSeverity(e.target.value)}>
            <option value="">All</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </label>

        <label>
          Search:
          <input value={q} onChange={e => setQ(e.target.value)} placeholder="employee name" />
        </label>

        <button onClick={load} disabled={loading}>{loading ? "Loading..." : "Refresh"}</button>
      </div>

      <table style={{ width: "100%", borderCollapse: "collapse" }} border={1}>
        <thead>
          <tr>
            <th>Employee</th><th>Category</th><th>Severity</th><th>Status</th><th>Created</th><th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map(a => (
            <tr key={a.id}>
              <td>{a.employee.name}</td>
              <td>{a.category}</td>
              <td>{a.severity}</td>
              <td>{a.status}</td>
              <td>{new Date(a.created_at).toLocaleString()}</td>
              <td>{a.status === "open" ? <button onClick={() => onDismiss(a.id)}>Dismiss</button> : null}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;










/*
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App*/
