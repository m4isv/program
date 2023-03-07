dotacao = 5.42

dollas = {10.75, 25, 100}

map = {}

for _,value in pairs(dollas) do
	table.insert(map, value * dotacao)
end

print(map[1])

