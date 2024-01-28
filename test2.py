from models.text.llama70 import llama70

response = llama70.create_req(
                prompt="Can you write a poem about open source machine learning? Let's make it in the style of E. E. Cummings.",
                )


print(response)


