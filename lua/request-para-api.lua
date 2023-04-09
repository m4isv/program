os.execute("clear")



--############################
--instalando Os Plugins
--apt install luarocks
--luarocks install luasocket
--luarocks install lua-cjson
--############################



local cjson = require("cjson")
local http = require("socket.http")


local response, status = http.request("http://ip-api.com/json/24.48.0.1")

local myTable = cjson.decode(response)

if status == 200 then
  local name = myTable.status
  local cidade = myTable.country

  print(name)
  print(cidade)



else
  print("Erro ao fazer requisição: " .. status)
end

