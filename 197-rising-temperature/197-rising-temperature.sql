SELECT W2.ID FROM Weather W1 JOIN Weather W2 ON DATEDIFF(W1.recordDate, W2.recordDate) = -1
WHERE W2.temperature > W1.temperature