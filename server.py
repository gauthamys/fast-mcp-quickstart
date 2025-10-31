from fastmcp import FastMCP

app = FastMCP(name="My FastMCP Server")

@app.resource("/hello")
async def hello(request):
    return {"message": "Hello, FastMCP!"}

@app.tool("/echo")
async def echo(request):
    data = await request.json()
    return {"echo": data}

if __name__ == "__main__":
    app.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
