def calculate_total(prices)
    total = 0

    prices.each do |price|
        total += price.to_f
    end

    puts "Total: $#{total.round(2)}"
end

prices = ["10.50", "20.25", "5.75"]

calculate_total(prices)