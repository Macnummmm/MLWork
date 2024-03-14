# Q4.1
training_errors = [3.28041, 2.84517, 2.84324, 0.06642, 0.06547, 0.01351, 0.00002, 0.00001, 0.00000]
validation_errors = [0.09207, 0.23039, 0.24427, 0.06274, 0.04612, 0.13232, 0.66764, 0.65973, 0.78241]

best_generalization_model = validation_errors.index(min(validation_errors))
print("Q4.1. The best generalization model =", best_generalization_model)

# Q4.2
most_overfitting_model = training_errors.index(max(training_errors))
print("Q4.2. The most overfitting model =", most_overfitting_model)

# Q4.3
models = ['A', 'B', 'C', 'D']
training_errors = [925.6229, 189.6254, 189.1378, 152.3213]
validation_errors = [1172.9233, 107.1493, 106.7562, 152.8397]

best_generalization_model = models[validation_errors.index(min(validation_errors))]
print("Q4.3. The best generalization model =", best_generalization_model)

# Q4.4
most_overfitting_model = models[training_errors.index(max(training_errors))]
print("Q4.4. The most overfitting model =", most_overfitting_model)
