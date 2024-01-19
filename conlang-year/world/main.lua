X = 0
Y = 0
SPEED = 100

function love.update(dt)
    if love.keyboard.isDown('up') then
        Y = Y - SPEED * dt
    elseif love.keyboard.isDown('down') then
        Y = Y + SPEED * dt
    end
    if love.keyboard.isDown('right') then
        X = X + SPEED * dt
    elseif love.keyboard.isDown('left') then
        X = X - SPEED * dt
    end
end

function love.draw()
    love.graphics.print("Hello world", X, Y)
end
