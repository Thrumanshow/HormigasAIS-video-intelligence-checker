-- xoxo_datetime.lua
-- Devuelve la fecha y hora actual en formato ISO 8601

function get_iso_datetime()
  return os.date("!%Y-%m-%dT%H:%M:%SZ")
end
