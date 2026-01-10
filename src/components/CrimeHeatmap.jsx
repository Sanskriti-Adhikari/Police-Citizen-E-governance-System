import React from 'react';
import { MapContainer, TileLayer, CircleMarker, Tooltip } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

// Mock crime data: lat/lng inside Kathmandu Valley
const crimeData = [
  { lat: 27.7172, lng: 85.3240, type: 'Theft', severity: 'High' },
  { lat: 27.7089, lng: 85.3210, type: 'Assault', severity: 'Medium' },
  { lat: 27.7140, lng: 85.3050, type: 'Burglary', severity: 'Low' },
  { lat: 27.7120, lng: 85.3200, type: 'Robbery', severity: 'High' },
];

export default function CrimeHeatmap() {
  return (
    <MapContainer center={[27.7172, 85.3240]} zoom={13} style={{ height: '100%', width: '100%' }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png" />
      {crimeData.map((crime, idx) => (
        <CircleMarker
          key={idx}
          center={[crime.lat, crime.lng]}
          radius={crime.severity === 'High' ? 12 : crime.severity === 'Medium' ? 8 : 5}
          color={crime.severity === 'High' ? 'red' : crime.severity === 'Medium' ? 'orange' : 'green'}
        >
          <Tooltip>{${crime.type} - ${crime.severity}}</Tooltip>
        </CircleMarker>
      ))}
    </MapContainer>
  );
}