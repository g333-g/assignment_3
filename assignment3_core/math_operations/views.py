from django.shortcuts import render

def math_form(request):
    if request.method == "POST":
        x = int(request.POST.get("x", 0))
        y = int(request.POST.get("y", 0))
        z = int(request.POST.get("z", 1))

        original_x = x

        x += y
        step1 = x
        x -= z
        step2 = x
        x *= y
        step3 = x
        x %= z
        step4 = x
        x = x / z if z != 0 else "undefined"
        step5 = x

        result = (step5 if isinstance(step5, (int, float)) else 0) + y + z

        return render(request, "result.html", {
            "original_x": original_x,
            "y": y,
            "z": z,
            "step1": step1,
            "step2": step2,
            "step3": step3,
            "step4": step4,
            "step5": step5,
            "result": result
        })

    return render(request, "math_form.html")
