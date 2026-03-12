import discord
import random
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Ha iniciado sesión como {bot.user}')



# ---- MENÚ DE TEMAS ----
@bot.command()
async def informacion(ctx):
    menu = (
        "🌎 **Temas sobre el medio ambiente**\n"
        "1️⃣ Contaminación ambiental\n"
        "2️⃣ Cambio climático\n"
        "3️⃣ Biodiversidad\n"
        "4️⃣ Reciclaje\n"
        "5️⃣ Energías renovables\n\n"
        "Escribe el número del tema."
    )
    await ctx.send(menu)



# ---- RESPUESTAS ----
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return



    # ---- MENÚ CONTAMINACIÓN ----
    if message.content == "1":
        await message.channel.send(
            "🏭 **Contaminación ambiental**\n"
            "Escribe un número del 1 al 5:\n"
            "1️⃣ Qué es la contaminación\n"
            "2️⃣ Contaminación del aire\n"
            "3️⃣ Contaminación del agua\n"
            "4️⃣ Contaminación del suelo\n"
            "5️⃣ Cómo reducirla"
        )

    elif message.content == "11":
        await message.channel.send("La contaminación ocurre cuando sustancias dañinas se introducen en el aire, el agua o el suelo, afectando a los seres vivos y al equilibrio del medio ambiente. Puede ser causada por actividades humanas como la industria, el transporte o el manejo inadecuado de residuos.")

    elif message.content == "12":
        await message.channel.send("Los vehículos y las fábricas liberan gases como dióxido de carbono y otros contaminantes que afectan la calidad del aire. Estos gases pueden provocar problemas respiratorios en las personas y contribuir al cambio climático.")

    elif message.content == "13":
        await message.channel.send("La basura que se arroja en ríos, lagos y mares contamina el agua y pone en peligro a peces, tortugas y muchas otras especies. Muchos animales pueden ingerir plásticos o quedar atrapados en ellos.")

    elif message.content == "14":
        await message.channel.send("El uso excesivo de pesticidas y productos químicos en la agricultura puede dañar el suelo, reducir su fertilidad y contaminar el agua subterránea, afectando también a plantas, animales y personas.")

    elif message.content == "15":
        await message.channel.send("Reciclar, reutilizar materiales y reducir el uso de plásticos son acciones que ayudan a disminuir la contaminación. También es importante separar los residuos y promover hábitos responsables con el medio ambiente.")



    # ---- MENÚ CAMBIO CLIMÁTICO ----
    elif message.content == "2":
        await message.channel.send(
            "🌡 **Cambio climático**\n"
            "Escribe un número del 1 al 5:\n"
            "21 Qué es\n"
            "22 Gases de efecto invernadero\n"
            "23 Causas\n"
            "24 Consecuencias\n"
            "25 Soluciones"
        )

    elif message.content == "21":
        await message.channel.send("El cambio climático es el aumento progresivo de la temperatura del planeta debido a alteraciones en el clima de la Tierra. Este fenómeno provoca cambios en los patrones de lluvia, temperatura y estaciones en diferentes regiones del mundo.")

    elif message.content == "22":
        await message.channel.send("Los gases de efecto invernadero, como el dióxido de carbono y el metano, atrapan el calor del Sol en la atmósfera. Esto hace que la temperatura del planeta aumente más de lo normal.")

    elif message.content == "23":
        await message.channel.send("La quema de combustibles fósiles como petróleo, carbón y gas en vehículos, fábricas y plantas de energía libera grandes cantidades de dióxido de carbono, uno de los principales responsables del cambio climático.")

    elif message.content == "24":
        await message.channel.send("El cambio climático puede causar sequías prolongadas, tormentas más intensas, olas de calor y el aumento del nivel del mar debido al derretimiento de los glaciares y los polos.")

    elif message.content == "25":
        await message.channel.send("Usar energías renovables como la solar, eólica o hidroeléctrica ayuda a reducir la emisión de gases contaminantes y contribuye a disminuir el impacto del cambio climático.")



    # ---- MENÚ BIODIVERSIDAD ----

    elif message.content == "3":
        await message.channel.send(
            "🦋 **Biodiversidad**\n"
            "Escribe: \n"
            "31 Que es la Biodiversidad\n"
            "32 Importancia\n"
            "33 Amenazas\n"
            "34 Proteccion\n"
            "35 Curiosidad"
        )
        
    elif message.content == "31":
        await message.channel.send("La biodiversidad es la variedad de seres vivos que existen en el planeta, incluyendo animales, plantas, hongos y microorganismos. También abarca la diversidad genética y los diferentes ecosistemas donde habitan.")

    elif message.content == "32":
        await message.channel.send("La biodiversidad mantiene el equilibrio de los ecosistemas, ya que cada especie cumple una función importante, como la polinización, el control de plagas o la descomposición de materia orgánica.")

    elif message.content == "33":
        await message.channel.send("La deforestación y la contaminación amenazan muchas especies al destruir sus hábitats naturales y alterar los ecosistemas donde viven, lo que puede llevar a la disminución o incluso a la extinción de algunas especies.")

    elif message.content == "34":
        await message.channel.send("Los parques naturales y las áreas protegidas ayudan a conservar ecosistemas, plantas y animales, evitando actividades humanas que puedan dañar la naturaleza y promoviendo la protección de la biodiversidad.")

    elif message.content == "35":
        await message.channel.send("Se estima que existen más de 8 millones de especies en la Tierra, aunque muchas aún no han sido descubiertas o estudiadas por los científicos.")



    # ---- MENÚ RECICLAJE ----
    
    elif message.content == "4":
        await message.channel.send(
            "♻ **Reciclaje**\n"
            "Escribe:\n"
            "41 Que es reciclar\n"
            "42 Materiales reciclables\n"
            "43 Beneficios\n"
            "44 Reducir residuos\n"
            "45 Reutilizar"
        )
        
    elif message.content == "41":
        await message.channel.send("Reciclar es el proceso de convertir residuos o materiales usados en nuevos productos, permitiendo que los materiales vuelvan a utilizarse y evitando que terminen como basura en el medio ambiente.")

    elif message.content == "42":
        await message.channel.send("Materiales como papel, vidrio, plástico y aluminio pueden reciclarse. Estos se recolectan, se procesan y se transforman en nuevos productos que pueden volver a utilizarse.")

    elif message.content == "43":
        await message.channel.send("El reciclaje reduce la contaminación, disminuye la cantidad de basura en vertederos y ahorra recursos naturales como agua, energía y materias primas.")

    elif message.content == "44":
        await message.channel.send("Reducir el consumo significa usar solo lo necesario y evitar el desperdicio. Esto ayuda a generar menos basura y a disminuir el impacto ambiental.")

    elif message.content == "45":
        await message.channel.send("Reutilizar objetos consiste en volver a usar productos o materiales en lugar de desecharlos, lo que ayuda a alargar su vida útil y a reducir la cantidad de residuos.")

    
    
    # ---- MENÚ ENERGIAS RENOVABLES ----
    
    elif message.content == "5":
        await message.channel.send(
            "⚡ **Energías renovables**\n"
            "Escribe:\n"
            "51 Qué son las energías renovables\n"
            "52 Energía solar\n"
            "53 Energía eólica\n"
            "54 Energía hidroeléctrica\n"
            "55 Importancia de las energías renovables"
        )

    elif message.content == "51":
        await message.channel.send("Las energías renovables son fuentes de energía que provienen de recursos naturales que se regeneran constantemente, como el sol, el viento o el agua, y que no se agotan fácilmente.")

    elif message.content == "52":
        await message.channel.send("La energía solar proviene del Sol y se obtiene mediante paneles solares que transforman la luz solar en electricidad o calor para diferentes usos.")

    elif message.content == "53":
        await message.channel.send("La energía eólica se genera a partir del viento. Los aerogeneradores o molinos de viento transforman la fuerza del viento en energía eléctrica.")

    elif message.content == "54":
        await message.channel.send("La energía hidroeléctrica se obtiene del movimiento del agua en ríos o represas. El flujo del agua mueve turbinas que generan electricidad.")

    elif message.content == "55":
        await message.channel.send("Las energías renovables son importantes porque reducen la contaminación, disminuyen el uso de combustibles fósiles y ayudan a proteger el medio ambiente.")
        
        
        
    await bot.process_commands(message)

bot.run("")
