from fastmcp import FastMCP

app = FastMCP(name="My FastMCP Server")

@app.tool("echo")
async def echo(request):
    data = await request.json()
    return {"echo": data}

@app.tool("test")
async def test(request):
    return {"status": "Test tool is working!"}

if __name__ == "__main__":
    app.run()
