Token = "" -- Buyer token (not need to be encrypted)

local Webhook = "" -- Webhook for logs (need to be encrypted)

AddEventHandler('onResourceStart', function(resourceName)
    if (GetCurrentResourceName() ~= resourceName) then return end
    PerformHttpRequest("https://api.myip.com/", function(err, text, headers)
        local ip = json.decode(text).ip
        if Token == nil then
            print("[Rockstar Services] Your Token Is Missing")
            Wait(5000)
            os.exit()
        end
        PerformHttpRequest("http://HOSTIP/tokens.php?token="..Token.."&ip="..ip.."", function(err, text, headers)
            if text == nil then
                print("[Rockstar Services] Api Is Down")
                Wait(5000)
                os.exit()
            end
            if text == "no" then 
                print('[Rockstar Services] Not Authorized')
                local embed = {
                    {
                        ["title"] = 'Product Started',
                        ["description"] = '**Product Name:** ' .. resourceName .. '\n**IP:** ' .. ip .. '\n**License:** ' .. Token .. '\n**Not Authorized | Triggered Server Crash **',
                        ["footer"] = {
                            ["text"] = "Made By Rockstar Services",
                        },
                    }
                }
                PerformHttpRequest(Webhook, function(err, text, headers) end, 'POST', json.encode({username = 'Rockstar Services', embeds = embed}), { ['Content-Type'] = 'application/json' })
                Wait(5000)
                os.exit()
            elseif text == "yes" then
                print('[Rockstar Services] Authorized')
                local embed = {
                    {
                        ["title"] = 'Product Started',
                        ["description"] = '**Product Name:** ' .. resourceName .. '\n**IP:** ' .. ip .. '\n**License:** ' .. Token .. '\n**Authorized | Yes **',
                        ["footer"] = {
                            ["text"] = "Made By Rockstar Services",
                        },
                    }
                }
                PerformHttpRequest(Webhook, function(err, text, headers) end, 'POST', json.encode({username = 'Rockstar Services', embeds = embed}), { ['Content-Type'] = 'application/json' })
            end
        end)
    end)
end)