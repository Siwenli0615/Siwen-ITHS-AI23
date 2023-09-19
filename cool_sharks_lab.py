{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPmkZE5/BD8UdYSudrrbrWQ",
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
        "<a href=\"https://colab.research.google.com/github/Siwenli0615/Hello-world/blob/main/cool_sharks_lab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "shark_list = [\"Hammerhead\", \"Blacktip\", \"Thresher\", \"Leopard\",\"Megamouth\"]\n",
        "# dubbelkollar med print:\n",
        "print(f\"test for shark_list:{shark_list}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gHxUdBZF1-D2",
        "outputId": "d737186f-40dd-4f9f-dbc3-de6a84c70183"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "test for shark_list:['Hammerhead', 'Blacktip', 'Thresher', 'Leopard', 'Megamouth']\n"
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
        "shark_list = [\"Hammerhead\", \"Blacktip\", \"Thresher\", \"Leopard\",\"Megamouth\"] # lista från uppgiften a)\n",
        "\n",
        "\n",
        "simplified_shark_test = []    # skapade en ny lista med nya variabel\n",
        "for name in shark_list:       # går igenom varje namn med for loop:\n",
        "  if len(name) >= 8:    # sparar in i ny lista för de namn >=8\n",
        "    simplified_shark_test.append(name)\n",
        "print(f\"simplified_shark_test: {simplified_shark_test}\")\n",
        "\n",
        "# nu göra om till listcomprehension:\n",
        "filtered_shark_names = [name for name in shark_list if len(name)>=8]\n",
        "\n",
        "# kontrollerar:\n",
        "print(f\"filtered_shark_names: {filtered_shark_names}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n4TUFLwU2dhS",
        "outputId": "b7cc08f7-9bd3-41ee-db7b-0b867c44c143"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "simplified_shark_test: ['Hammerhead', 'Blacktip', 'Thresher', 'Megamouth']\n",
            "filtered_shark_names: ['Hammerhead', 'Blacktip', 'Thresher', 'Megamouth']\n"
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
        "# listan från b) uppgiften:\n",
        "filtered_shark_names = ['Hammerhead', 'Blacktip', 'Thresher', 'Megamouth']\n",
        "\n",
        "# börjar med att räkna bokstäver i varje namn:\n",
        "shark_with_number_test = []\n",
        "for name in filtered_shark_names:\n",
        "  shark_with_number_test.append([name,len(name)])\n",
        "\n",
        "print(f\"shark_with_number_test: {shark_with_number_test}\")\n",
        "\n",
        "# Göra om till list comprehension:\n",
        "sharks_with_numbers = [[name,len(name)] for name in filtered_shark_names]\n",
        "print(f\"sharks_with_numbers:    {sharks_with_numbers}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p7bMsgxf-xRX",
        "outputId": "50a83a47-e5b4-4d3d-b4d7-1b8559dfaa86"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "shark_with_number_test: [['Hammerhead', 10], ['Blacktip', 8], ['Thresher', 8], ['Megamouth', 9]]\n",
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
        "# listan från c)\n",
        "sharks_with_numbers = [['Hammerhead', 10], ['Blacktip', 8], ['Thresher', 8], ['Megamouth', 9]]\n",
        "\n",
        "# test:\n",
        "for name,number in sharks_with_numbers:\n",
        "  print(f\"**{name.upper()} har {number} bokstäver!**\")\n",
        "print()\n",
        "# list comprehension:\n",
        "print(\"\\n\".join([f\"**{name.upper()} har {number} bokstäver!**\" for name,number in sharks_with_numbers]))\n",
        "# det blir en \"{None}\" extra efter eftertraktad listan, bollade lite för att få det rätta format..."
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sVTcuYzsQUuS",
        "outputId": "300f29f5-f61a-42fd-ffcb-58be3f0e6404"
      },
      "execution_count": 4,
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
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Qwjb91HLYx-O"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}