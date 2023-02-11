from google.cloud import aiplatform

endpoint = aiplatform.Endpoint(
    endpoint_name="projects/{PROJECT ID}/locations/{REGION}/endpoints/{ENDPOINT ID}"
)

test_mpg = [1.4838871833555929,
 1.8659883497083019,
 2.234620276849616,
 1.0187816540094903,
 -2.530890710602246,
 -1.6046416850441676,
 -0.4651483719733302,
 -0.4952254087173721,
 0.7746763768735953]

response = endpoint.predict([test_mpg])

print('API response: ', response)

print('Predicted MPG: ', response.predictions[0][0])