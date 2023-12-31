{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN64Ep57fx8WVG8Zu2aM067",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Siwenli0615/Hello-world/blob/main/cool_sharks_lab_siwen.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Lab-uppgift: Python List Comprehensions"
      ],
      "metadata": {
        "id": "wAb9Noy117Ly"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" Uppgift: a) Skapa en lista av hajarna du sett \"\"\"\n",
        "\n",
        "# döper till namn \"sharks\"\n",
        "sharks = [\"Hammerhead\", \"Blacktip\", \"Thresher\", \"Leopard\",\"Megamouth\"]\n",
        "# dubbelkollar med print:\n",
        "print(f\"test:{sharks}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gHxUdBZF1-D2",
        "outputId": "785d403f-74e1-4849-cd5d-dc201e77c5d7"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "test:['Hammerhead', 'Blacktip', 'Thresher', 'Leopard', 'Megamouth']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" b) Uppgift: Använd en listkomprehension på listan från a) som\n",
        "filtrerar ut namnet på den haj som har färre än 8 bokstäver\n",
        "i sitt namn. Lagra den resulterande listan i en ny variabel.\n",
        "\"\"\"\n",
        "\n",
        "# Plan: först förstå och få rätt med en lista, därefter göra till\n",
        "# list comprehension.\n",
        "\n",
        "sharks = [\"Hammerhead\", \"Blacktip\", \"Thresher\", \"Leopard\",\"Megamouth\"] # lista från uppgiften a)\n",
        "\n",
        "\n",
        "simplified_shark_test = []    # skapade en ny lista med nya variabel\n",
        "for name in sharks:       # går igenom varje namn:\n",
        "  if len(name) >= 8:    # sparar in i ny lista för de namn >=8\n",
        "    simplified_shark_test.append(name)\n",
        "print(f\"simplified_shark_test: {simplified_shark_test}\")\n",
        "\n",
        "# nu göra om till listcomprehension:\n",
        "simplified_shark_list = [name for name in sharks if len(name)>=8]\n",
        "\n",
        "# kontrollerar:\n",
        "print(f\"simplified_shark_list: {simplified_shark_list}\")\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n4TUFLwU2dhS",
        "outputId": "6f24ddfa-e3d9-4993-e08c-c7fa2cac6c01"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "simplified_shark_test: ['Hammerhead', 'Blacktip', 'Thresher', 'Megamouth']\n",
            "simplified_shark_list: ['Hammerhead', 'Blacktip', 'Thresher', 'Megamouth']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" c) Beräkna bokstavsantal för varje haj:\n",
        "Använd en listkomprehension på listan från b) som genererar en lista av listor,\n",
        "där varje lista innehåller växtens namn och antalet bokstäver i namnet. Lagra\n",
        "denna lista i en ytterligare ny variabel.\"\"\"\n",
        "\n",
        "# Plan: vi börjar med att försöka förstå, sen utveckla.\n",
        "\n",
        "# börjar med att räkna bokstäver i varje namn:\n",
        "sharp_with_number_test = []\n",
        "for name in simplified_shark_list:\n",
        "  sharp_with_number_test.append([name,len(name)])\n",
        "\n",
        "print(f\"sharp_with_number_test: {sharp_with_number_test}\")\n",
        "\n",
        "# Göra om till list comprehension:\n",
        "sharks_with_numbers = [[name,len(name)] for name in simplified_shark_list]\n",
        "print(f\"sharks_with_numbers:    {sharks_with_numbers}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p7bMsgxf-xRX",
        "outputId": "5948d06a-007b-4b9f-d749-28d15df7e935"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sharp_with_number_test: [['Hammerhead', 10], ['Blacktip', 8], ['Thresher', 8], ['Megamouth', 9]]\n",
            "sharks_with_numbers:    [['Hammerhead', 10], ['Blacktip', 8], ['Thresher', 8], ['Megamouth', 9]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\" d) Uppgift: Använd en for-loop på listan från c), för att skriva ut följande:\n",
        "**HAMMERHEAD har 10 bokstäver!**\n",
        "**BLACKTIP har 8 bokstäver!**\n",
        "osv\n",
        "\"\"\"\n",
        "\n",
        "for name,number in sharks_with_numbers:\n",
        "  print(f\"**{name.upper()} har {number} bokstäver!**\")\n",
        "print()\n",
        "# om man vill ha på list comprehension:\n",
        "{print(f\"**{name.upper()} har {number} bokstäver!**\") for name,number in sharks_with_numbers}\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sVTcuYzsQUuS",
        "outputId": "b1b24159-8f7f-49f2-e3db-3364eaa9f4ec"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "**HAMMERHEAD har 10 bokstäver!**\n",
            "**BLACKTIP har 8 bokstäver!**\n",
            "**THRESHER har 8 bokstäver!**\n",
            "**MEGAMOUTH har 9 bokstäver!**\n",
            "\n",
            "**HAMMERHEAD har 10 bokstäver!**\n",
            "**BLACKTIP har 8 bokstäver!**\n",
            "**THRESHER har 8 bokstäver!**\n",
            "**MEGAMOUTH har 9 bokstäver!**\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{None}"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    }
  ]
}