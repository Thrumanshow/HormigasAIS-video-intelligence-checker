-- Integración Lua para RIME / XOXO - HormigasAIS
-- Archivo: xoxo_datetime.lua

-- Traducido y adaptado para HormigasAIS
-- Módulo de respuesta contextual inteligente con fecha y día actual

local function yield_cand(seg, text)
  local cand = Candidate("", seg.start, seg._end, text, "")
  cand.quality = 100
  yield(cand)
end

local M = {}

function M.init(env)
  local config = env.engine.schema.config
  env.name_space = env.name_space:gsub("^*", "")
  M.xoxo_trigger = config:get_string(env.name_space .. "/xoxo_datetime") or "xoxo"
end

function M.func(input, seg, env)
  if (input == M.xoxo_trigger) then
    local t = os.time()
    yield_cand(seg, os.date("Hoy es: %Y-%m-%d", t))
    yield_cand(seg, os.date("Hora actual: %H:%M", t))
    yield_cand(seg, os.date("Día de la semana: %A", t))
    yield_cand(seg, os.date("🌐 XOXO - HormigasAIS • %Y-%m-%d %H:%M", t))
  end
end

return M
